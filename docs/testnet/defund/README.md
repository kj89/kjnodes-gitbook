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

**live-peers** (27)
```
peers="156eb5692a8ea7252ea58fecf82781fc23a6f29e@109.123.246.107:26656,182cf8af05a1883553b797552eb2a9bab5836713@65.109.84.216:36656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,2d3d11ac1f96ffb54c1df3000ed1c73684507a3b@144.91.80.32:40656,fd40c978275ceb1e0f9a81a7f40b3ec5f8b7b544@195.201.237.184:36656,d130db7a4901fd92a221f1cf7d006c6153751eb5@144.76.27.79:60956,c2ec4dbc771adbefdbdefa0edf4750687725236d@151.106.35.182:26656,eaa27fa4ac25781ae7ba9a43d04f10c5890898fc@154.53.52.32:40656,d1d1f9b34c3e4d46d7268588848b59b3a696a533@194.233.66.70:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,0362d884e6687401ab93555ff099af4a07f614d5@46.101.90.33:26656,bb25b67fd12c5b08b6d949eb21d1a3a865307e1e@95.111.243.155:40656,fb73921dc5bf1e939308eaa37053c12bd647852b@45.147.199.210:26656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,0c0772f5c52a95412208acfa579ef5adb4266ec1@92.38.241.107:26656,25d9dc04057628c83a3fe2406af9f1882e3ecf61@45.147.199.62:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,77b3dcacd513f7f7fa1b0247d716f464ad61e94d@65.109.65.210:34656,676a37bdffc3ad213bfa47ec24e20bc5fc4cfd7e@95.216.211.140:26656,77a7c437c7e0c421eeaebe677235306d2466da4c@91.194.11.156:26656,04bdf241c94c3d59c34b5496b012279f099a6cca@168.119.89.31:33656,114d6ed1ee640298baa1a695367e9e9189078154@92.119.112.231:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,90dc33a14889c0a0348b18a03d2a3d0eab41e6cb@92.119.112.225:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
