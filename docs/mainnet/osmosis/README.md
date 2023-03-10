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

**live-peers** (32)
```bash
peers="c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,b56ec345ef591b57ffc8657116f4b045ab6b35fd@188.40.98.155:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,616327f7ca045fb57827683e471ca472a232ef1f@89.33.8.233:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,1876eb08c7e93c965a895177f82c8725f89c0f65@54.214.183.228:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,e3cc05de734a9eb3da832cf0236f319a9a4063ba@95.216.101.39:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,60a2c89e7253502e93517a026f44a2431cc81230@220.85.113.39:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,31e7a8b8cc97e85472c609f9d220fdd9536d4f4d@94.130.220.54:26656,b37a3c92c039de2582edd120b16afa3f462ecf3e@23.88.69.22:27166,925d0be14f6332d0515744d88c232aff209ca8c5@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
