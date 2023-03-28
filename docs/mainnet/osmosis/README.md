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

**live-peers** (23)
```bash
peers="e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,e929ea43bf60adfcc79ef7f973e70b92ccef21fe@18.159.135.176:26656,dc230c6475bdbf3ab64058a37a8de2261b6396eb@74.96.207.58:26822,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,d8e616474295a62dbbe831d1552873401ae0c2a5@65.108.121.110:16656,f52f76f144c93e0e8313dce465b8c00afe2fc4e6@89.149.218.123:26656,d6b066c4b91768fccc9df1012876b53a239d9fa9@3.15.176.200:26656,91729592f49f871d6eacde0c721a8f104119c902@52.12.69.48:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
