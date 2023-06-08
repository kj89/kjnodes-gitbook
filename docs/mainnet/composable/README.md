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

**live-peers** (24)
```bash
peers="4cb008db9c8ae2eb5c751006b977d6910e990c5d@65.108.71.163:2630,724fb9c02f28390abdf371ff4914609f1890a3fc@95.216.39.183:10656,92336725dc7fda1504ea5962bb551f2610126377@65.108.198.118:22256,27f9f5c65d626e2756ca8deea23e4dc3608126e3@65.109.154.181:30656,8d70f16094502dcc6a6fb1065b9ab9c958c266d6@65.109.104.72:22256,253f190c96d14ce98da8b7596385c1593a7be982@65.109.33.48:23656,211a8dd121f7de6e2ed53efe87cba194d0637d49@65.108.8.247:22256,548b18f0288f4c128ef3ff133dcadf004263c363@38.242.230.118:26656,186c1eed9dd4a1fb1acc35236237d3992ed3250e@188.165.205.120:15956,77975a9a8117248712cdb0b371accfff2a686182@15.235.40.124:26656,efe99b4c22402e91fe630c0c747fe17528e79134@89.58.53.67:26656,4319824b0ff4c795ec8c48e09f504fbe97c8a6e7@142.132.135.125:20656,3f72dfcaa83c4922dd6e72bc5b9da7840ef8adaa@57.128.96.155:22256,690a53df99c570aef22106bca3b77bec2881bf32@65.21.139.155:26656,f1417ea1b17234f37ebb67f6ef55aea791e591e8@142.44.213.82:1400,2cba1a83afb55d9a86cbbb5054a09e82a768df29@65.21.88.12:2000,63559b939442512ed82d2ded46d02ab1021ea29a@95.214.55.138:53656,72e97d478faa181dfbf9c5043b0005b4f339f283@38.146.3.171:22256,2f62b3a091af9b81d5f7060fdb2e33aac5805faa@65.109.69.154:31656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.140:26976,c7f52f81ee1b1f7107fc78ca2de476c730e00be9@65.109.80.150:2635,e361a46ab3211b09e65a9afa791ae08f040bff16@195.154.94.166:23931,7ea064d6aa7e54afa00d6354e923eece322363b8@193.26.159.34:39656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
