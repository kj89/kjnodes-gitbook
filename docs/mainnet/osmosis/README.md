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
peers="9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,e3cc05de734a9eb3da832cf0236f319a9a4063ba@95.216.101.39:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,b04794731b9aa16d1aab035b58c2012e9a0fea8b@50.21.167.184:26656,fc2ad6fb9f20b4a637e244d92c35362bdb5d96af@100.26.145.135:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,2736d870197d443e463b4ff4b7b52f1cec920030@45.63.39.14:26656,fced2c95050c0d4781b76cd2b0a93efae03cb395@65.108.77.93:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,77cd623e9d68d664141fb8b6b0817150fe78ca08@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
