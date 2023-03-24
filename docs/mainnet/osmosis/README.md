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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,8c914ce925e8e5290a5caa07edf71875eba653a1@18.159.135.176:26656,7c95763aa711ae9750342c528990856e974d6d34@3.15.176.200:26656,be95e2acd1dcb6c2c56a5690d36a307d9807835d@52.12.69.48:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
