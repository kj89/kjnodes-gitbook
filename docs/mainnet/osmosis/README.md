# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


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

**live-peers** (23)
```bash
peers="3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,8c65f3e86e701cac8336ba572e114b711ed08629@141.94.242.239:26656,9f2489016bcf055fde40498f54bf893f3a00f9de@138.201.85.176:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,cf1cb007704715f3d3eaa0fa08868ad08ff5e6a0@18.159.135.176:26656,364997b92c05b05d5ddb151915eeed2229e686d8@52.12.69.48:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,a89eb7c8be27db87f23fb39e9423cbf2e260b80f@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
