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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,fc2ad6fb9f20b4a637e244d92c35362bdb5d96af@100.26.145.135:26656,173751092c573b78d0dd40677dc7d7f5b546dcfd@94.130.207.9:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,d90150d606724bb19d533f861024174f3aa42351@213.239.213.115:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,82588f011491c6100d922d133f52fc23460b9231@95.217.91.234:26656,1876eb08c7e93c965a895177f82c8725f89c0f65@54.214.183.228:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,071ae914b06e14148a6286a0fa087c797336f043@34.105.246.121:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,786ab2f9fd97aeda1c6c2fb8f83e84ff5fbd0eea@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
