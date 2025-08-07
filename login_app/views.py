from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import Group
from .forms_plantao import PassagemPlantaoForm, CentralMonitoramentoForm
from .models_plantao import PassagemPlantao, CentralMonitoramento
from .forms_cftv import PassageCFTVForm
from .models_cftv import PassageCFTV
import pandas as pd
import plotly.express as px

from django.http import HttpResponseForbidden

@login_required
def passagem_plantao(request):
    if not request.user.groups.filter(name='operadorescm').exists():
        return HttpResponseForbidden('Acesso restrito ao grupo operadorescm.')
    return render(request, 'passagem_plantao.html')


@login_required
def dashboard_view(request):
    if not request.user.groups.filter(name='gerentes').exists():
        return HttpResponseForbidden('Acesso restrito ao grupo gerentes.')
    return render(request, 'dashboard.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        # Garante que o usuário está autenticado
        if not user.is_authenticated:
            return '/login/'
        # Redireciona conforme grupo
        if user.groups.filter(name='operadorescm').exists():
            return '/passagem_plantao/'
        elif user.groups.filter(name='gerentes').exists() or user.groups.filter(name='gerentes').exists():
            return '/dashboard/'
        elif user.groups.filter(name='operadorescftv').exists():
            return '/passagem_cftv/'
        else:
            return '/dashboard/'

# View para exibir e salvar o formulário de passagem de plantão
# Salva no banco plantao_db via router

def passagem_plantao_view(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        plantao = request.POST.get('plantao')
        base = request.POST.get('base')
        total_veiculos = request.POST.get('total_veiculos')
        veiculos_pernoite = request.POST.get('veiculos_pernoite')
        veiculos_viagem = request.POST.get('veiculos_viagem')
        veiculos_manutencao = request.POST.get('veiculos_manutencao')
        veiculos_cliente = request.POST.get('veiculos_cliente')
        desvios_rota = request.POST.get('desvios_rota')
        observacoes = request.POST.get('observacoes')
        # Novos campos
        rotas_embarcadas = request.POST.get('rotas_embarcadas')
        veiculos_para_iniciar_viagem = request.POST.get('veiculos_para_iniciar_viagem')
        veiculos_postos_fiscais = request.POST.get('veiculos_postos_fiscais')
        veiculos_borracharias = request.POST.get('veiculos_borracharias')
        sinistros = request.POST.get('sinistros')
        parada_nao_autorizada = request.POST.get('parada_nao_autorizada')
        veiculos_abandonados = request.POST.get('veiculos_abandonados')
        veiculos_bloqueados_inatividade = request.POST.get('veiculos_bloqueados_inatividade')
        perda_sinal = request.POST.get('perda_sinal')
        rotas_embarcadas_3s = request.POST.get('rotas_embarcadas_3s')
        rotas_embarcadas_t4s = request.POST.get('rotas_embarcadas_t4s')
        tem_mouse_pad = request.POST.get('tem_mouse_pad')
        tem_descanso_pe = request.POST.get('tem_descanso_pe')
        tem_carregador = request.POST.get('tem_carregador')
        nome_coordenador = request.POST.get('nome_coordenador')
        nome_usuario = request.POST.get('nome_usuario')
        try:
            total_veiculos = int(total_veiculos) if total_veiculos else 0
            veiculos_pernoite = int(veiculos_pernoite) if veiculos_pernoite else 0
            veiculos_viagem = int(veiculos_viagem) if veiculos_viagem else 0
            veiculos_manutencao = int(veiculos_manutencao) if veiculos_manutencao else 0
            veiculos_cliente = int(veiculos_cliente) if veiculos_cliente else 0
            desvios_rota = int(desvios_rota) if desvios_rota else 0
            rotas_embarcadas = int(rotas_embarcadas) if rotas_embarcadas else 0
            veiculos_para_iniciar_viagem = int(veiculos_para_iniciar_viagem) if veiculos_para_iniciar_viagem else 0
            veiculos_postos_fiscais = int(veiculos_postos_fiscais) if veiculos_postos_fiscais else 0
            veiculos_borracharias = int(veiculos_borracharias) if veiculos_borracharias else 0
            sinistros = int(sinistros) if sinistros else 0
            parada_nao_autorizada = int(parada_nao_autorizada) if parada_nao_autorizada else 0
            veiculos_abandonados = int(veiculos_abandonados) if veiculos_abandonados else 0
            veiculos_bloqueados_inatividade = int(veiculos_bloqueados_inatividade) if veiculos_bloqueados_inatividade else 0
            perda_sinal = int(perda_sinal) if perda_sinal else 0
            rotas_embarcadas_3s = int(rotas_embarcadas_3s) if rotas_embarcadas_3s else 0
            rotas_embarcadas_t4s = int(rotas_embarcadas_t4s) if rotas_embarcadas_t4s else 0
            tem_mouse_pad = bool(tem_mouse_pad)
            tem_descanso_pe = bool(tem_descanso_pe)
            tem_carregador = bool(tem_carregador)
        except Exception as e:
            return render(request, 'passagem_plantao.html', {'error': f'Erro ao converter campos numéricos: {e}'})
        # Salva na tabela centralMonitoramento do banco plantao_db
        CentralMonitoramento.objects.using('plantao_db').create(
            data=data,
            plantao=plantao,
            base=base,
            total_veiculos=total_veiculos,
            veiculos_pernoite=veiculos_pernoite,
            veiculos_viagem=veiculos_viagem,
            veiculos_manutencao=veiculos_manutencao,
            veiculos_cliente=veiculos_cliente,
            desvios_rota=desvios_rota,
            rotas_embarcadas=rotas_embarcadas,
            veiculos_para_iniciar_viagem=veiculos_para_iniciar_viagem,
            veiculos_postos_fiscais=veiculos_postos_fiscais,
            veiculos_borracharias=veiculos_borracharias,
            sinistros=sinistros,
            parada_nao_autorizada=parada_nao_autorizada,
            veiculos_abandonados=veiculos_abandonados,
            veiculos_bloqueados_inatividade=veiculos_bloqueados_inatividade,
            perda_sinal=perda_sinal,
            rotas_embarcadas_3s=rotas_embarcadas_3s,
            rotas_embarcadas_t4s=rotas_embarcadas_t4s,
            tem_mouse_pad=tem_mouse_pad,
            tem_descanso_pe=tem_descanso_pe,
            tem_carregador=tem_carregador,
            observacoes=observacoes,
            usuario=request.user.username,
            nome_coordenador=nome_coordenador,
            nome_usuario=nome_usuario,
        )
        return redirect('login')  # Redireciona para tela de login após salvar
    return render(request, 'passagem_plantao.html')

def dashboard_view(request):

    from django.utils import timezone
    from datetime import timedelta
    agora = timezone.now()
    limite = agora - timedelta(hours=36)
    dados = CentralMonitoramento.objects.filter(data_envio__gte=limite).values()
    df = pd.DataFrame(dados)
    # Filtra o DataFrame para garantir que só mostre dados das últimas 36 horas na tabela (usando data_envio original)
    if 'data_envio' in df.columns:
        import pytz
        tz_sp = pytz.timezone('America/Sao_Paulo')
        # Converte data_envio para datetime com timezone de SP
        df['data_envio_dt'] = pd.to_datetime(df['data_envio'], utc=True).dt.tz_convert(tz_sp)
        agora_sp = pd.Timestamp.now(tz=tz_sp)
        limite_sp = agora_sp - pd.Timedelta(hours=36)
        # Filtra o DataFrame ANTES de qualquer formatação
        df = df[df['data_envio_dt'] >= limite_sp]
        # Atualiza a coluna data (caso ela exista) para garantir consistência na tabela
        if 'data' in df.columns:
            df['data'] = df['data_envio_dt'].dt.strftime('%Y-%m-%d')
        # Só depois de filtrar, formata para string para exibição
        df['data_envio'] = df['data_envio_dt'].dt.strftime('%H:%M:%S')
        df = df.drop(columns=['data_envio_dt'])

    if df.empty:
        return render(request, 'dashboard/index.html', {
            'grafico1': "<p>Sem dados</p>",
            'grafico2': "",
            'grafico3': "",
            'grafico4': "",
            'grafico5': "",
            'grafico6': "",
            'grafico7': "",
            'grafico8': "",
            'grafico9': "",
            'grafico10': "",
            'grafico11': ""
        })
    # 1. Rotas embarcadas por base (normal / 3S / T4S) - gráfico de pizza para proporção
    df_grouped = df.groupby('base')[['rotas_embarcadas', 'rotas_embarcadas_3s', 'rotas_embarcadas_t4s']].sum().reset_index()
    rename_dict = {
        'rotas_embarcadas': 'Rotas outras Tec',
        'rotas_embarcadas_3s': 'Rotas 3S',
        'rotas_embarcadas_t4s': 'Rotas T4S'
    }
    df_grouped = df_grouped.rename(columns=rename_dict)
    df_pizza = df_grouped[list(rename_dict.values())].sum().reset_index()
    df_pizza.columns = ['Tipo de Rota', 'Quantidade']
    # Paleta de cores padrão do logo
    palette = ["#008E00", "#A1D900", "#E6FF05", "#A1A1A1"]
    grafico1 = px.pie(
        df_pizza,
        names='Tipo de Rota',
        values='Quantidade',
        title='Proporção de Rotas Embarcadas (Outras Tec. / 3S / T4S)',
        color_discrete_sequence=palette
    )

    # 2. Veículos em manutenção por base
    grafico2 = px.line(
        df.groupby('base')['veiculos_manutencao'].sum().reset_index().rename(columns={'veiculos_manutencao': 'Em Manutenção'}),
        x='base',
        y='Em Manutenção',
        title='Veículos em Manutenção por Base',
        markers=True,
        line_shape="linear",
        color_discrete_sequence=palette
    )

    # 3. Veículos em postos fiscais por base
    grafico3 = px.bar(
        df.groupby('base')['veiculos_postos_fiscais'].sum().reset_index().rename(columns={'veiculos_postos_fiscais': 'Em Postos Fiscais'}),
        x='base',
        y='Em Postos Fiscais',
        title='Veículos em Postos Fiscais por Base',
        color_discrete_sequence=palette
    )

    # 4. Veículos em viagem por base
    grafico4 = px.bar(
        df.groupby('base')['veiculos_viagem'].sum().reset_index().rename(columns={'veiculos_viagem': 'Em Viagem'}),
        x='base',
        y='Em Viagem',
        title='Veículos em Viagem por Base',
        color_discrete_sequence=palette
    )

    # 5. Contador total de sinistros
    total_sinistros = int(df['sinistros'].sum())
    grafico5 = f'<div style="font-size:2.2rem;font-weight:bold;color:#d32f2f;text-align:center; 0;">Total de Sinistros: {total_sinistros}</div>'

    total_veiculos_viagem = int(df['veiculos_viagem'].sum())
    grafico12 = f'<div style="font-size:2.2rem;font-weight:bold;color:#d32f2f;text-align:center; 0;">Total de Veículos em Viagem: {total_veiculos_viagem}</div>'
    # 6. Quantidade de formulários enviados por base
    grafico6 = px.bar(
        df.groupby('base').size().reset_index(name='Formulários Enviados'),
        x='base',
        y='Formulários Enviados',
        title='Quantidade de Formulários Enviados por Base',
        color_discrete_sequence=palette
    )

    # 7. Sinistros por data (dd/mm/aaaa) - gráfico de linha para evolução temporal
    df['data_str'] = pd.to_datetime(df['data']).dt.strftime('%d/%m/%Y')
    grafico7 = px.line(
        df.groupby('data_str')['sinistros'].sum().reset_index().rename(columns={'sinistros': 'Sinistros', 'data_str': 'Data'}),
        x='Data',
        y='Sinistros',
        title='Sinistros por Data (dd/mm/aaaa)',
        markers=True,
        color_discrete_sequence=palette
    )

    # 8. Veículos em borracharias por base
    grafico8 = px.bar(
        df.groupby('base')['veiculos_borracharias'].sum().reset_index().rename(columns={'veiculos_borracharias': 'Em Borracharias'}),
        x='base',
        y='Em Borracharias',
        title='Veículos em Borracharias por Base',
        color_discrete_sequence=palette
    )

    # 9. Veículos bloqueados por base
    grafico9 = px.bar(
        df.groupby('base')['veiculos_bloqueados_inatividade'].sum().reset_index().rename(columns={'veiculos_bloqueados_inatividade': 'Bloqueados'}),
        x='base',
        y='Bloqueados',
        title='Veículos Bloqueados por Base',
        color_discrete_sequence=palette
    )

    # 10. Veículos em clientes por base
    grafico10 = px.bar(
        df.groupby('base')['veiculos_cliente'].sum().reset_index().rename(columns={'veiculos_cliente': 'Em Clientes'}),
        x='base',
        y='Em Clientes',
        title='Veículos em Clientes por Base',
        color_discrete_sequence=palette
    )

    # 11. Top 5 bases com maior quantidade de veículos - barras horizontais para ranking
    df['total_veiculos_soma'] = df[['veiculos_viagem', 'veiculos_pernoite', 'veiculos_manutencao', 'veiculos_postos_fiscais', 'veiculos_borracharias']].sum(axis=1)
    top5 = df.groupby('base')['total_veiculos_soma'].sum().reset_index().sort_values(by='total_veiculos_soma', ascending=False).head(5)
    top5 = top5.rename(columns={'total_veiculos_soma': 'Total de Veículos'})
    grafico11 = px.bar(
        top5,
        x='Total de Veículos',
        y='base',
        orientation='h',
        title='Top 5 Bases com Mais Veículos',
        color_discrete_sequence=palette
    )

    # 12. Relação das últimas 15 passagens de plantão (todos os campos relevantes)
    # Campos para exibir na tabela
    campos_tabela = ['nome_usuario', 'data', 'data_envio', 'base', 'nome_coordenador']  # manter o campo, mas mudar o cabeçalho na tabela
    # Campos para mostrar no modal (todos os detalhes)
    campos_detalhe = [
        'nome_coordenador', 'nome_usuario', 'data', 'data_envio', 'plantao', 'base', 'total_veiculos', 'veiculos_pernoite', 'veiculos_viagem', 'veiculos_manutencao',
        'veiculos_cliente', 'desvios_rota', 'rotas_embarcadas', 'veiculos_para_iniciar_viagem', 'veiculos_postos_fiscais',
        'veiculos_borracharias', 'sinistros', 'parada_nao_autorizada', 'veiculos_abandonados', 'veiculos_bloqueados_inatividade',
        'perda_sinal', 'rotas_embarcadas_3s', 'rotas_embarcadas_t4s', 'tem_mouse_pad', 'tem_descanso_pe', 'tem_carregador',
        'observacoes'
    ]
    # Todas as passagens das últimas 48h para tabela
    # Remove duplicidade de colunas
    campos_unicos = []
    for campo in campos_tabela + campos_detalhe:
        if campo not in campos_unicos:
            campos_unicos.append(campo)
    # Filtra o DataFrame para garantir que só mostre dados das últimas 36 horas na tabela
    if 'data_envio' in df.columns:
        from django.utils import timezone
        from datetime import timedelta
        import pytz
        tz_sp = pytz.timezone('America/Sao_Paulo')
        agora = timezone.now().astimezone(tz_sp)
        limite = agora - timedelta(hours=36)
        # Converte data_envio para datetime com timezone de SP
        df_dt = pd.to_datetime(df['data_envio'], format='%H:%M:%S', errors='coerce')
        # Como só temos o horário, não é possível filtrar por data exata aqui, então filtramos pelo DataFrame original
        if 'data_envio' in df.columns:
            # Filtra pelo campo original antes de formatar para string
            if 'data_envio' in dados.model._meta.fields_map:
                # Se for um campo DateTimeField
                df = df[pd.to_datetime(df['data_envio'], utc=True).dt.tz_convert(tz_sp) >= limite]
            else:
                # Se for string, não filtra
                pass
    relacao_formularios = df[campos_unicos].sort_values(by='data', ascending=False)
    # Gera tabela apenas com os campos visíveis, mas inclui os detalhes em atributos data-* para o modal
    linhas = []
    for _, row in relacao_formularios.iterrows():
        # Monta atributos data-* para todos os campos de detalhe
        data_attrs = ' '.join([f'data-{campo}="{str(row[campo]).replace(chr(34), "&quot;")}"' for campo in campos_detalhe])
        # Monta linha da tabela
        linha = f'<tr {data_attrs}>' + ''.join([f'<td>{row[campo]}</td>' for campo in campos_tabela]) + '</tr>'
        linhas.append(linha)
    # Cabeçalho da tabela
    # Personaliza o cabeçalho para mostrar 'Horário' ao invés de 'Data Envio'
    cabecalhos_personalizados = {
        'data_envio': 'Horário',
    }
    cabecalho = ''.join([
        f'<th>{cabecalhos_personalizados.get(campo, campo.replace("_", " ").title())}</th>'
        for campo in campos_tabela
    ])
    tabela_formularios = f'<table class="tabela-formularios"><thead><tr>{cabecalho}</tr></thead><tbody>' + ''.join(linhas) + '</tbody></table>'

    context = {
        'grafico1': grafico1.to_html(full_html=False),
        'grafico2': grafico2.to_html(full_html=False),
        'grafico3': grafico3.to_html(full_html=False),
        'grafico4': grafico4.to_html(full_html=False),
        'grafico5': grafico5,  # já é HTML seguro
        'grafico6': grafico6.to_html(full_html=False),
        'grafico7': grafico7.to_html(full_html=False),
        'grafico8': grafico8.to_html(full_html=False),
        'grafico9': grafico9.to_html(full_html=False),
        'grafico10': grafico10.to_html(full_html=False),
        'grafico11': grafico11.to_html(full_html=False),
        'tabela_formularios': tabela_formularios,
        'grafico12': grafico12,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
@csrf_protect

def passagem_cftv_view(request):
    if not request.user.groups.filter(name='operadorescftv').exists():
        return HttpResponseForbidden('Acesso restrito ao grupo operadorescftv.')
    if request.method == 'POST':
        form = PassageCFTVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PassageCFTVForm()
    return render(request, 'passagem_cftv.html', {'form': form})