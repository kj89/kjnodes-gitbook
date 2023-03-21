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
peers="1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,31e7a8b8cc97e85472c609f9d220fdd9536d4f4d@94.130.220.54:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
