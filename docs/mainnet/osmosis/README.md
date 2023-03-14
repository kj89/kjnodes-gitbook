# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v14.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)




## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: [https://osmosis.grpc.kjnodes.com](https://osmosis.grpc.kjnodes.com)

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

**live-peers** (33)
```bash
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,797094953d830f8727f3b5175f2b205df16d5867@45.77.212.231:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,e3cc05de734a9eb3da832cf0236f319a9a4063ba@95.216.101.39:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,f5f8a3ba560fafd7c34efa95aed96d27fece3f19@3.15.176.200:26656,f3122fc41bf61b22a5a3c309a8478d2602425ec3@3.34.181.188:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
