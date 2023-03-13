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
peers="1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,b04794731b9aa16d1aab035b58c2012e9a0fea8b@50.21.167.184:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,2736d870197d443e463b4ff4b7b52f1cec920030@45.63.39.14:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,60a2c89e7253502e93517a026f44a2431cc81230@220.85.113.39:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,e81c3c20833cfb5d652a9c842c9f1c8b1835479d@108.61.190.21:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,25e30bd2612ca5f8e1cff4825b8ffc59267f760f@3.15.176.200:26656,c4071f5639de601d581850774805477dc3171d69@190.192.133.218:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
