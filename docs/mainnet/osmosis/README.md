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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,9f2489016bcf055fde40498f54bf893f3a00f9de@138.201.85.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,b37a3c92c039de2582edd120b16afa3f462ecf3e@23.88.69.22:27166,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,7c28e9f02c998d84a4f617c3852b7794dc2883fd@88.99.253.55:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,7eea530e720ca2e5ae2b4e6324d4f2a6303fc753@157.90.93.137:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,120908ac6e79df7ad48b3954474afeca0401682a@141.94.248.63:26656,60a2c89e7253502e93517a026f44a2431cc81230@220.85.113.39:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,6ace63806ffb2f54c601857b3f972636b683cb27@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
