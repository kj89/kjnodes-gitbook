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
peers="c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,d8e616474295a62dbbe831d1552873401ae0c2a5@65.108.121.110:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,ee768420a22d4cbe3a4d1bea43ae914fd5f0e080@18.159.135.176:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,fae586d242e4b293c7eae765a10f1c933675b5e8@3.15.176.200:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,7c5459ea4bbc41aa4d86ffe8126f0651155227c8@85.195.102.127:26656,3441b5525d75ee3b8e747903c26376de34d53fbe@52.12.69.48:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
