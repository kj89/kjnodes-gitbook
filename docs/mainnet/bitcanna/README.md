# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.1 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: [https://bitcanna.grpc.kjnodes.com](https://bitcanna.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (20)
```bash
peers="846fca7d90fdc1ddbcf1892a0b6338a44e93b76d@65.108.0.93:36656,cb0848b84987c37ba0fa465585c6b9d6cec6deab@65.108.77.98:26696,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
