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
* grpc: osmosis.grpc.kjnodes.com:29090

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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,43785e5ffd8783393ea8094f77efcee5bdbcdce3@78.141.244.18:26656,bfb67b2ae345955d6bc0991450120669c683386e@149.56.25.66:26656,47e4075978458bfc382630b2a46aabbbbf7977b2@143.198.234.114:26656,20913e92e8b9ea2d80ad34edd9b52e97886cf616@54.37.30.181:26656,a6283307952423c1751431c220d11ed36b61ed84@143.110.237.113:26656,30e9432879d5b0976b88e52120dc12338e40fc33@65.108.108.176:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e0fbdbdce6ec8797412751edd00fbaf114c42fad@34.220.226.204:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,724cef11bbe866269b3d67f7dd5ea539cc4096bf@198.244.164.186:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,407267ac44b20a0a4258d0bbca1c9f657bf88d08@74.118.143.19:26656,e81c3c20833cfb5d652a9c842c9f1c8b1835479d@108.61.190.21:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,2736d870197d443e463b4ff4b7b52f1cec920030@45.63.39.14:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,bc7ad831ef3e5c91a8570d2bf3548be4d7d587a1@18.159.135.176:26656,15f13f67865d93235c1dfc9f6b9390f9c24d0559@3.15.176.200:26656,d8e616474295a62dbbe831d1552873401ae0c2a5@65.108.121.110:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
