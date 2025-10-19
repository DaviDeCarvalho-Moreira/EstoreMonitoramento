from app.components.scrap_method import ScrapPrices



### URLS DE PESQUISA

MONITOR_KABUM = 'https://www.kabum.com.br/produto/472908/monitor-gamer-curvo-lg-ultragear-34-wqhd-ultrawide-160hz-1ms-freesync-premium-hdr10-som-integrado-34gp63a-b'
GABINETE_PICHAU = 'https://www.pichau.com.br/gabinete-gamer-corsair-frame-4500x-lx-r-rgb-mid-tower-lateral-de-vidro-preto-cc-9011316-ww'
VIDEO = 'https://www.terabyteshop.com.br/produto/34802/placa-de-video-sapphire-pure-amd-radeon-rx-7700-xt-frostpunk-2-limited-edition-12gb-gddr6-fsr-ray-tracing-11335-08-50g'


MOUSE_KABUM = 'https://www.kabum.com.br/produto/883179/mouse-gamer-sem-fio-attack-shark-x11-22000-dpi-59g-tri-modo-com-dock-magnetico-rgb-branco'
FONTE_PICHAU = 'https://www.pichau.com.br/fonte-cooler-master-mwe-gold-650-v3-650w-atx-3-1-80-plus-gold-preto-mpe-6502-acaag-3bbr'
PROCESSADOR_TERABYTE = 'https://www.terabyteshop.com.br/produto/25440/processador-amd-ryzen-3-4100-38ghz-40ghz-turbo-4-cores-8-threads-cooler-wraith-stealth-am4-100-100000510box'



def main():
    
    SP = ScrapPrices()
    
   
    # a = SP.kabum_scrap(MONITOR_KABUM)
    # b = SP.pichau_scrap(GABINETE_PICHAU)
    # c = SP.terabyte_scrap(VIDEO)
    # print(a,b,c)
    
    # d = SP.kabum_scrap(MOUSE_KABUM)
    # e = SP.pichau_scrap(FONTE_PICHAU)
    f = SP.terabyte_scrap(PROCESSADOR_TERABYTE)
    print(f)



if __name__ == "__main__":
    main()
