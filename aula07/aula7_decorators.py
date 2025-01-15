from loguru import logger

logger.add("meu_app.log")

def soma(a, b) -> int:
    logger.info(a)
    logger.info(b)
    logger.info(a + b)
    return a + b

print(soma(2, 3))