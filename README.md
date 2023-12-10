# Projeto---Processamento-de-Imagens
Projeto desenvolvido para a disciplina de Processamento de Imagens da Universidade Tecnológica Federal do Paraná

<sub>Este arquivo README está sendo seguindo a estrutura proposta pelo professor da disciplina<sub>

## Processando Imagens com HU Moments e/ou LBP

**Integrante: William da Cruz Pires**

### Descritores

**Descritor - Hu Moments:**

Os momentos de Hu são um conjunto de sete invariantes em relação à escala, rotação e reflexão, derivados dos momentos geométricos de uma imagem. Eles capturam características de forma e são calculados a partir dos momentos invariantes de Zernike. Os Hu Moments fornecem uma representação compacta da forma de um objeto, sendo robustos a variações de escala e orientação. Sua importância reside na capacidade de descrever características de forma de maneira invariante, o que é crucial em tarefas de reconhecimento de padrões e classificação de objetos.

<sub>*Zernike foi um físico neerlandês que criou o microscópio de contraste de fase<sub>

**Descritor - Local Binary Pattern (LBP):**

O LBP é um descritor de textura que mede padrões locais de variação de intensidade em uma imagem. Ele opera atribuindo um código binário a cada pixel com base na comparação de sua intensidade com a intensidade dos pixels vizinhos. O LBP é calculado para cada pixel, gerando um padrão binário que reflete as características locais da textura. Este descritor é eficaz na representação de texturas distintas e é amplamente utilizado em aplicações como reconhecimento facial, detecção de texturas e classificação de imagens.

**Importância para este Projeto:**

***Hu Moments:*** Esses "momentos" serão eficazes para capturar características de forma específicas nas imagens, permitindo ao classificador aprender padrões que são invariantes a rotações, escalas e reflexões. Isso é crucial em projetos onde a orientação e o tamanho dos objetos podem variar.

***LBP:*** O LBP será útil para capturar informações de textura nas imagens. Em muitos projetos, a textura desempenha um papel importante na diferenciação entre diferentes classes de objetos ou padrões. O LBP, sendo um descritor de textura robusto, complementará os Hu Moments na representação abrangente das características das imagens.

<sub>Os dois descritores estão presentes no projeto, mas não sendo utilizados ambos (mesmo sabendo que isso proporcionaria ao classificador uma representação mais rica e abrangente das imagens). Fica a escolha do usuário utilizar o que preferir alterando a função a ser utilizada.<sup>

### Classificador

**Random Forest:**

O Random Forest é um algoritmo de aprendizado de máquina que pertence à categoria de métodos ensemble. O termo "ensemble" refere-se à ideia de combinar as previsões de vários modelos para melhorar o desempenho geral do sistema. No caso do Random Forest, esses modelos individuais são árvores de decisão.

**Importância para o Projeto:**

No contexto do projeto, o Random Forest é escolhido como classificador devido à sua capacidade de lidar com conjuntos de dados complexos, robustez a overfitting e bom desempenho geral em tarefas de classificação. Ele é particularmente útil quando há características diversas e pode ser ajustado para incorporar diferentes descritores, como Hu Moments e LBP, para melhorar a representação e classificação de padrões nas imagens

### Bibliotecas Utilizadas

<sub>É necessário ter o Mini Conda instalado. Após isto basta instalar as bibliotecas por linha de comando no ambiente que será utilizado<sub>

```python
import cv2
import numpy
import sklearn
import matplotlib
import skimage
```

**<sub>*Esta são bibliotecas __essenciais__ para processamento de imagens.<sub>**

<sub>As bibliotecas a seguir são bibliotecas adicionais que, foram necessário para a minha aplicação:<sub>

```python
import os
import time
import datetime
from progress.bar import Bar
```

***<sup>Deve executar o projeto no ambiente do miniconda (após a instalação de todas as bibliotecas).<sup>***
