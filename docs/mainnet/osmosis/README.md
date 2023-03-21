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

**live-peers** (20)
```bash
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,e3cc05de734a9eb3da832cf0236f319a9a4063ba@95.216.101.39:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,31e7a8b8cc97e85472c609f9d220fdd9536d4f4d@94.130.220.54:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
