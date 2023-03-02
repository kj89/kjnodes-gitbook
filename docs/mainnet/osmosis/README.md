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

**live-peers** (33)
```bash
peers="a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,2000928f1b09973431b53292ef80c1cd836fd967@168.119.213.117:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,e3cc05de734a9eb3da832cf0236f319a9a4063ba@95.216.101.39:26656,fd0930fea06876e362e0a92046854ed651f27ac2@45.76.13.41:26656,797094953d830f8727f3b5175f2b205df16d5867@45.77.212.231:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,9f2489016bcf055fde40498f54bf893f3a00f9de@138.201.85.176:26656,5e9051d2ae7d9be1656a5348ad0916f255b96c73@135.181.214.17:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,b04794731b9aa16d1aab035b58c2012e9a0fea8b@50.21.167.184:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,616327f7ca045fb57827683e471ca472a232ef1f@89.33.8.233:26656,0dc90bfcac46048ba0e0e0f2bd4ed6bd6474ccd9@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
