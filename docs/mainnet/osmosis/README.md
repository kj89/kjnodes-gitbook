# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (21)
```bash
peers="f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,b653dc7cb255eff0e79cd8dfc9b2a04672a7f758@18.159.135.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
