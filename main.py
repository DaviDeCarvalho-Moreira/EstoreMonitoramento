from app.components.scrap_method import ScrapPrices



### URLS DE PESQUISA

MONITOR_KABUM = 'https://www.kabum.com.br/produto/472908/monitor-gamer-curvo-lg-ultragear-34-wqhd-ultrawide-160hz-1ms-freesync-premium-hdr10-som-integrado-34gp63a-b'
GABINETE_PICHAU = 'https://www.pichau.com.br/gabinete-gamer-corsair-frame-4500x-lx-r-rgb-mid-tower-lateral-de-vidro-preto-cc-9011316-ww'
VIDEO = 'https://www.terabyteshop.com.br/produto/34802/placa-de-video-sapphire-pure-amd-radeon-rx-7700-xt-frostpunk-2-limited-edition-12gb-gddr6-fsr-ray-tracing-11335-08-50g'


def main():
    
    SP = ScrapPrices()
    
    
    a = SP.kabum_scrap(MONITOR_KABUM)
    b = SP.pichau_scrap(GABINETE_PICHAU)
    c = SP.terabyte_scrap(VIDEO)
    print(a,b,c)




if __name__ == "__main__":
    main()
