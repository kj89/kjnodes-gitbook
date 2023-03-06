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
peers="71f2451869d7363ce5d91366143de63069641303@65.108.71.166:33656,d90150d606724bb19d533f861024174f3aa42351@213.239.213.115:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,7eea530e720ca2e5ae2b4e6324d4f2a6303fc753@157.90.93.137:26656,e81c3c20833cfb5d652a9c842c9f1c8b1835479d@108.61.190.21:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,9f2489016bcf055fde40498f54bf893f3a00f9de@138.201.85.176:26656,616327f7ca045fb57827683e471ca472a232ef1f@89.33.8.233:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,5e9051d2ae7d9be1656a5348ad0916f255b96c73@135.181.214.17:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,071ae914b06e14148a6286a0fa087c797336f043@34.105.246.121:26656,259ab883ee76f92e82f8f14d463aaaa09d857fb9@144.76.70.108:9010,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,60a2c89e7253502e93517a026f44a2431cc81230@220.85.113.39:26656,7a2a74f392f7896a5547aba232c06a2c032d3dcc@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
