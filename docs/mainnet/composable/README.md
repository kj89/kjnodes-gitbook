# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: centauri-1 | **Latest Version Tag**: v2.3.5 | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable](https://explorer.kjnodes.com/composable)

## Public endpoints

* api: [https://composable.api.kjnodes.com](https://composable.api.kjnodes.com)
* rpc: [https://composable.rpc.kjnodes.com](https://composable.rpc.kjnodes.com)
* grpc: composable.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@composable.rpc.kjnodes.com:15956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@composable.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (30)
```bash
peers="c6eefdcc5cbe41dd457183c7c3bd7311ddf97638@65.109.116.119:16156,92336725dc7fda1504ea5962bb551f2610126377@65.108.198.118:22256,253f190c96d14ce98da8b7596385c1593a7be982@65.109.33.48:23656,f1417ea1b17234f37ebb67f6ef55aea791e591e8@142.44.213.82:1400,548b18f0288f4c128ef3ff133dcadf004263c363@38.242.230.118:26656,4cb008db9c8ae2eb5c751006b977d6910e990c5d@65.108.71.163:2630,690a53df99c570aef22106bca3b77bec2881bf32@65.21.139.155:26656,1617a476e3a883c2e648ee91120ffecefbbe3a19@65.109.115.119:26656,efe99b4c22402e91fe630c0c747fe17528e79134@89.58.53.67:26656,6201b6958ac3151c53e88c438aa80c42c5b3f740@65.108.238.29:22256,8d70f16094502dcc6a6fb1065b9ab9c958c266d6@65.109.104.72:22256,3f72dfcaa83c4922dd6e72bc5b9da7840ef8adaa@57.128.96.155:22256,72e97d478faa181dfbf9c5043b0005b4f339f283@38.146.3.171:22256,2cba1a83afb55d9a86cbbb5054a09e82a768df29@65.21.88.12:2000,e3cd5d7925fc390e34a05129a30409db62cbd2d7@185.119.118.118:3000,3b27aab10ded3765aeb8f3dc70e0f7b2581e4196@141.95.157.139:22256,211a8dd121f7de6e2ed53efe87cba194d0637d49@65.108.8.247:22256,042a5b6dd173322ef238d11fb6561ca3947ed24c@139.99.208.77:26676,17bfb555c37b79e89af31342f4e068bf4f93e144@65.108.137.39:26656,9e34b95377a50fb64dd86d2f95007c201f58a8e4@94.130.240.229:3000,63559b939442512ed82d2ded46d02ab1021ea29a@95.214.55.138:53656,5d0406a0e0be147b7cab72fc13d2d84b7a15fc46@188.166.250.32:26656,c7f52f81ee1b1f7107fc78ca2de476c730e00be9@65.109.80.150:2635,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.140:26976,5983e226c8f8ddfe3199d3b8ad016ef961c95a0e@51.91.30.173:3100,a7bd2dcc7204997bfa79918873b5eff994e66802@103.180.28.98:26656,90bde5c9bb575384ebb0d0d818dfa14198ae83f6@195.154.94.166:26339,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15956,1478b221f03d34f4643377ed0b975aef03dc0fe4@85.117.241.213:26656,4319824b0ff4c795ec8c48e09f504fbe97c8a6e7@142.132.135.125:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
