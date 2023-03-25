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

**live-peers** (22)
```bash
peers="1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,6d90149707d4f30cf3a3c5eb7df87febe49b0fc4@18.159.135.176:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,ea1d351267ad8921c8dd985010a5c85fded03f80@3.15.176.200:26656,51aecbca8fff8bca0fade96c26d1565c4ac868ad@52.12.69.48:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
