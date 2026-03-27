import math

def verificar_decolagem():
    erros = []

    print("Inicializando a verificação de decolagem...")

#input dos dados
    temp_interna = float(input("Digite a temperatura interna em (°C): "))
    temp_externa = float(input("Digite a temperatura externa em (°C): "))
    cap_total = float(input("Digite a capacidade total da bateria em (kWh): "))
    carga_atual = float(input("Digite a carga atual da bateria em (%): "))
    p_a = float(input("Digite a pressão do tanque A (PSI): "))   
    p_b = float(input("Digite a pressão do tanque B (PSI): "))
    status_mod = input("Digite o status do sistema de controle, Ignição, Comunicação, Entre outros. (OK/ERRO): ").upper()
    #consumo de viagem estático
    consumo_viagem = 400

    #calculos

    delta_t = abs(temp_interna - temp_externa)
    diferencial_p = abs(p_a - p_b)

    #definindo a eficiencia baseada na temperatura

    eficiencia = 0.95 if 0 <= temp_externa <= 40 else 0.85

    energia_total = cap_total * (carga_atual / 100) * eficiencia
    energia_util = energia_total * eficiencia

    #definindo integridade
    integridade = 1 if delta_t <= 60 else 0

    #decisoes 

    if integridade == 0:
        erros.append(f"Falha Estrutural: Delta T crítico ({delta_t}°C)")

    if p_a < 45 or p_a > 55 or p_b < 45 or p_b > 55:
        erros.append("Pressão dos tanques fora da margem (45-55 PSI)")

    if diferencial_p > 5:
        erros.append(f"Assimetria de pressão detectada: {diferencial_p} PSI")
        
    if energia_util < consumo_viagem:
        erros.append(f"Energia insuficiente: {energia_util:.2f}kWh disponíveis")
        
    if status_mod != "OK":
        erros.append("Módulos críticos com falha reportada")

#final
        print("\n" + "="*30)
    if not erros:
        print("STATUS: PRONTO PARA DECOLAR!")
        print(f"Energia Útil: {energia_util:.2f}kWh | Integridade: OK")
    else:
        print("STATUS: DECOLAGEM ABORTADA!")
        for erro in erros:
            print(f"- {erro}")
    print("="*30)

verificar_decolagem()



