# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (19)
```
peers="ec80e423e75ae61ecd24bf29f0a9b0720070e074@78.46.106.75:26656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,ba7d98b76435f2dad0b499429b730b817ddf85e1@45.147.199.214:26656,fe32ed5f0a7f8928f8299d8dd78fc5b650472ac4@65.108.46.123:56656,c55bf5597637964690e4255c1e78d81d848ca51f@65.108.252.216:36656,3b5ae4ac36564af240b96a135eddfe856966960c@5.9.22.14:60956,5a879e335d22f190dc614488a6a657874b66e260@62.171.162.229:36656,63f84e13148befd235d28b3e46b1de2da0aa99d8@176.9.167.181:26696,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,29ac18dffb64164b849b8ec9a29e0d3c32faa86b@62.171.183.6:26656,667f6c6d694bcd6743e6f42bb6e5996c4c9f16dd@84.244.31.1:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,50ab3cea5a763fed15f18dff1f35a503f88994b2@193.203.203.27:26656,ef4cac7e5813a753239239e297efcabc03a07fbb@194.180.176.125:26656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,fb73921dc5bf1e939308eaa37053c12bd647852b@45.147.199.210:26656,0362d884e6687401ab93555ff099af4a07f614d5@46.101.90.33:26656,cdd1107a3f013e4bfdd8e549e94b7e54ec18bd09@142.132.199.236:23656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
