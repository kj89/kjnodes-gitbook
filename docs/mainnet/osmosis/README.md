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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,dc230c6475bdbf3ab64058a37a8de2261b6396eb@74.96.207.58:26822,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,5ea9ac6872e057b0e285474c89ffb954653e3007@52.12.69.48:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,b2f9afdb8932f6b8cead8ca186473ed37d410881@3.15.176.200:26656,9a5cad2189ff3ec771c0634c6d3b9f2ec6fc4e4c@18.159.135.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
