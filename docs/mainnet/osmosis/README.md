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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,071ae914b06e14148a6286a0fa087c797336f043@34.105.246.121:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,7c28e9f02c998d84a4f617c3852b7794dc2883fd@88.99.253.55:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,5df599127784a7f220856ed370c9569e6b735d5f@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
