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

**live-peers** (29)
```
peers="507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,4e1527a2cc0e42bb15ff296df11f569e44a6d100@94.130.97.149:26656,bad21eb0dd7d2002912acc42a89b66a0deb44a03@65.21.134.202:26576,84c120f1b65467320292ff0a88f453f24079196e@65.109.82.75:36656,ba7d98b76435f2dad0b499429b730b817ddf85e1@45.147.199.214:26656,182cf8af05a1883553b797552eb2a9bab5836713@65.109.84.216:36656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@168.119.227.28:36656,fdb34ea011301410cf6231307287df27befe7049@85.114.142.242:46656,5a1977f1db820b7ee4719abbbff6f721f14176eb@65.109.84.254:36656,ef4cac7e5813a753239239e297efcabc03a07fbb@194.180.176.125:26656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,f8b6e9e0c424197192b0574dbfb536a62b357cfb@195.201.237.175:18656,09f8d04b89d6ed15e216a4c7f5469f42d5b90f9b@195.201.241.25:40656,24be58ab07ed513a64b359174c6bb6a17fa112d4@65.109.17.86:41656,5a879e335d22f190dc614488a6a657874b66e260@62.171.162.229:36656,5b6efed49f2d1d51a29a2a1fe5d40a5417aa8578@95.216.100.241:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,29ac18dffb64164b849b8ec9a29e0d3c32faa86b@62.171.183.6:26656,e734f373258a3c12d8c89a99e7d1124efc93ecab@185.250.148.41:26656,9dd904e70deef1042fc8a0802381fb083f83dc39@5.199.143.159:26656,b5252eac7b8bc4d5d2cc211bc794f8b4e62d2cc4@188.34.154.116:26656,cd53ab15aa53f7fd0f584bb60b253a4d53246867@93.189.30.116:26656,2c4ddd8d4af5405618098648864d1d9975024aa3@95.216.173.157:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,31a76ee9a69f97b5bbfe31494d5e159495d1cebb@5.161.127.97:26656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,606f26956b8387de65010b6fe74cc06b5989c5de@178.63.8.245:60656,667f6c6d694bcd6743e6f42bb6e5996c4c9f16dd@84.244.31.1:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
