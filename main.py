from app.components.scrap_method import ScrapPrices
from app.components.email_sender import email_sender
from app.models.email_info import remetente,password,destinatario,subject,message



### URLS DE PESQUISA

# Kabum
MONITOR_KABUM = 'https://www.kabum.com.br/produto/472908/monitor-gamer-curvo-lg-ultragear-34-wqhd-ultrawide-160hz-1ms-freesync-premium-hdr10-som-integrado-34gp63a-b'
MOUSE_KABUM = 'https://www.kabum.com.br/produto/883179/mouse-gamer-sem-fio-attack-shark-x11-22000-dpi-59g-tri-modo-com-dock-magnetico-rgb-branco'
PS_KABUM = 'https://www.kabum.com.br/produto/922662/console-sony-playstation-5-edicao-digital-ssd-825gb-controle-sem-fio-dualsense-2-jogos-digitais-1000050614'
NINTENDO_KABUM = 'https://www.kabum.com.br/produto/779788/console-nintendo-switch-2-jogo-digital-mario-kart-world'
NOTEBOOK_KABUM = 'https://www.kabum.com.br/produto/728904/notebook-lenovo-loq-e-core-i5-12450hx-rtx-3050-16gb-512gb-ssd-15-6-fhd-ips-144hz-win-11-luna-cinza-83me0007br'
# Pichau
GABINETE_PICHAU = 'https://www.pichau.com.br/gabinete-gamer-corsair-frame-4500x-lx-r-rgb-mid-tower-lateral-de-vidro-preto-cc-9011316-ww'
FONTE_PICHAU = 'https://www.pichau.com.br/fonte-cooler-master-mwe-gold-650-v3-650w-atx-3-1-80-plus-gold-preto-mpe-6502-acaag-3bbr'

# Terabyte
VIDEO_TERABYTE = 'https://www.terabyteshop.com.br/produto/34802/placa-de-video-sapphire-pure-amd-radeon-rx-7700-xt-frostpunk-2-limited-edition-12gb-gddr6-fsr-ray-tracing-11335-08-50g'
PROCESSADOR_TERABYTE = 'https://www.terabyteshop.com.br/produto/25440/processador-amd-ryzen-3-4100-38ghz-40ghz-turbo-4-cores-8-threads-cooler-wraith-stealth-am4-100-100000510box'

def main():
    
    SP = ScrapPrices()
    
#     SP.kabum_scrap(MOUSE_KABUM)
#     SP.kabum_scrap(NOTEBOOK_KABUM)
    
    
#     #PICHAU
#     SP.pichau_scrap(GABINETE_PICHAU)
#     SP.pichau_scrap(FONTE_PICHAU)
    
    
#     #TERABYTE
#     SP.terabyte_scrap(PROCESSADOR_TERABYTE)
    
    email_sender(remetente,
                 password,
                 destinatario,
                 subject,
                 message,
                )


if __name__ == "__main__":
    main()
