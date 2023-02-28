# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (29)
```bash
peers="f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,4d310dc74ecf838b4af1dc3cfcc88cdfdabb0eaa@139.177.202.235:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,b15ff06834de16016d8d905162e1365423d21a66@35.172.193.124:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,7c28e9f02c998d84a4f617c3852b7794dc2883fd@88.99.253.55:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,fced2c95050c0d4781b76cd2b0a93efae03cb395@65.108.77.93:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,259ab883ee76f92e82f8f14d463aaaa09d857fb9@144.76.70.108:9010,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
