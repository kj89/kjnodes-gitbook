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
peers="9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,f52f76f144c93e0e8313dce465b8c00afe2fc4e6@89.149.218.123:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,71f2451869d7363ce5d91366143de63069641303@65.108.71.166:33656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,b37a3c92c039de2582edd120b16afa3f462ecf3e@23.88.69.22:27166,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,10f328a43a1ac7aeeae7ee34c1127ce6839e4265@15.235.13.139:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,45335c203f9466400ae5383489d075023cae7757@52.12.69.48:26656,8e516a896de7aed4f757ee15c8a1d9f80d25774b@18.159.135.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
