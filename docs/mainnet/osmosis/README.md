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

**live-peers** (24)
```bash
peers="1876eb08c7e93c965a895177f82c8725f89c0f65@54.214.183.228:26656,2d283a97c4d3d85abd9782ab56f2919066d0878f@3.15.176.200:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,b04794731b9aa16d1aab035b58c2012e9a0fea8b@50.21.167.184:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
