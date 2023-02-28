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

**live-peers** (31)
```bash
peers="980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,ab0ad165e8485203eeb419795d228b016e0a67a9@195.201.172.9:15609,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,00b8417664577f3d66b27120523e7b6fd0d2e41f@54.214.82.222:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,7c5459ea4bbc41aa4d86ffe8126f0651155227c8@85.195.102.127:26656,259ab883ee76f92e82f8f14d463aaaa09d857fb9@144.76.70.108:9010,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,2736d870197d443e463b4ff4b7b52f1cec920030@45.63.39.14:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,7eea530e720ca2e5ae2b4e6324d4f2a6303fc753@157.90.93.137:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,5e9051d2ae7d9be1656a5348ad0916f255b96c73@135.181.214.17:26656,071ae914b06e14148a6286a0fa087c797336f043@34.105.246.121:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
