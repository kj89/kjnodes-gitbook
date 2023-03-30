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

**live-peers** (22)
```bash
peers="42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,d90150d606724bb19d533f861024174f3aa42351@213.239.213.115:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,751a7ea551745cbf9535691c1016988c5e6f4238@52.12.69.48:26656,04d38bc86fe4c7863ed2a650701a475659f0418b@3.15.176.200:26656,bedffc81ab89948b1cdde9af4577bf47bde08ff4@18.159.135.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
