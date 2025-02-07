#Estudo de caso do Bob Esponja fazendo hamburguers e milk-shake:
    # chapar o pao
    # fritar o hamburguer
    # montar o sanduiche
    # fazer o milk-shake

# Primeiro com utilizando o Sync(síncrono):
    # (Cada tarefa de uma vez)

from time import sleep

class SyncSpongeBob:
    def cook_bread(self):
        sleep(3)
        pao_na_chapa = 'Colocando o Pão na Chapa.'
        sleep(3)
        pao_pronto = 'O Pão está pronto'
        return pao_na_chapa, pao_pronto

    def cook_hamburger(self):
        sleep(10)
        hamburguer_na_chapa = 'Colocando o Hamburguer na Chapa.'
        sleep(10)
        hamburguer_pronto = 'O Hamburguer está Pronto'
        return hamburguer_na_chapa, hamburguer_pronto

    def mount_sandwich(self):
        sleep(3)
        montando_sanduiche = 'Montando o Sanduiche.'
        sleep(3)
        sanduiche_pronto = 'O Sanduiche está pronto.'
        return montando_sanduiche, sanduiche_pronto

    def make_milkshake(self):
        sleep(5)
        montando_milkshake = 'Montando o Milk-Shake.'
        sleep(5)
        milkshake_pronto = 'O Milk-Shake está pronto.'
        return montando_milkshake, milkshake_pronto

    def prepare_all(self):
        resultado_pao = self.cook_bread()
        resultado_hamburguer = self.cook_hamburger()
        resultado_sanduiche = self.mount_sandwich()
        resultado_milkshake = self.make_milkshake()

        print(resultado_pao)
        print(resultado_hamburguer)
        print(resultado_sanduiche)
        print(resultado_milkshake)
    
# sync_spongebob = SyncSpongeBob()
# sync_spongebob.prepare_all()

    # Segundo utilizando o metodo Async(Asincrono):
import asyncio

class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)
        pao_na_chapa = 'Colocando o Pão na Chapa.'
        await asyncio.sleep(3)
        pao_pronto = 'O Pão está pronto'
        return pao_na_chapa, pao_pronto

    async def cook_hamburger(self):
        await asyncio.sleep(10)
        hamburguer_na_chapa = 'Colocando o Hamburguer na Chapa.'
        await asyncio.sleep(10)
        hamburguer_pronto = 'O Hamburguer está Pronto'
        return hamburguer_na_chapa, hamburguer_pronto

    async def mount_sandwich(self):
        await asyncio.sleep(3)
        montando_sanduiche = 'Montando o Sanduiche.'
        await asyncio.sleep(3)
        sanduiche_pronto = 'O Sanduiche está pronto.'
        return montando_sanduiche, sanduiche_pronto

    async def make_milkshake(self):
        await asyncio.sleep(5)
        montando_milkshake = 'Montando o Milk-Shake.'
        await asyncio.sleep(5)
        milkshake_pronto = 'O Milk-Shake está pronto.'
        return montando_milkshake, milkshake_pronto

    async def cook(self):
        results = await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger(),
            self.make_milkshake()
        )
        sandwich_result = await self.mount_sandwich()

        print("Pão:", results[0])
        print("Hamburguer:", results[1])
        print("Milk-Shake:", results[2])
        print("Sanduíche:", sandwich_result)

if __name__ == '__main__':
    async_spongebob = AsyncSpongeBob()
    asyncio.run(async_spongebob.cook())