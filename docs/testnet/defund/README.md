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

**live-peers** (30)
```
peers="966e31c78c08aae8c74aa12702126141fb9cef7a@185.165.240.179:24666,d9db9bfb1e317bd16935b01a2227b699889519af@65.108.102.70:46656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,5f27d363c126cf7f7e1e9cab2dadd62862109e3d@65.21.227.112:26656,7da687fa5a1f9a635fb333519582fcc6fdada112@135.181.89.99:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,fd40c978275ceb1e0f9a81a7f40b3ec5f8b7b544@195.201.237.184:36656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,3441bf28387afc7d9b6e7a754c3ed37f21006859@5.161.134.231:26656,0f8c0605d9b8004332fbcaeaaababbbf9002e4df@135.181.253.11:18656,4d2f9132892d172b79cf00937fd554bd0f6a263c@92.119.112.200:26656,2d3d11ac1f96ffb54c1df3000ed1c73684507a3b@144.91.80.32:40656,d1d1f9b34c3e4d46d7268588848b59b3a696a533@194.233.66.70:26656,84c120f1b65467320292ff0a88f453f24079196e@65.109.82.75:36656,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656,156eb5692a8ea7252ea58fecf82781fc23a6f29e@109.123.246.107:26656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,24be58ab07ed513a64b359174c6bb6a17fa112d4@65.109.17.86:41656,31a76ee9a69f97b5bbfe31494d5e159495d1cebb@5.161.127.97:26656,997da62262006ce89d5019b7820b5552118e0df2@138.201.17.11:28656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,182cf8af05a1883553b797552eb2a9bab5836713@65.109.84.216:36656,db1b1a1350e3bf1815603024dc7dcc4ef76053b6@65.109.82.106:40656,ac7f2212b75a01fc6c7f19ca6365a6c4b4e90cf7@88.99.122.229:26656,b3a1fda2347ffc225121793b91edd132abdcc2d9@45.147.199.63:26656,26975c5bb7dc42463cc6361ea3c75f325e801917@5.161.86.214:18656,1d382998b8e596883cc788d09ba133f0e6bc96d3@65.21.104.54:36656,90dc33a14889c0a0348b18a03d2a3d0eab41e6cb@92.119.112.225:26656,324c36dcc39039d6c8007711b5923b4645c93202@142.132.202.50:46656,ae5a27e2e43174a2d161a8f7f8f019225ed328a0@178.170.41.148:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
