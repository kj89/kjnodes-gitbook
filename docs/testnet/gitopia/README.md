# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: gitopia-testnet.grpc.kjnodes.com:14190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:14156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:14159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (10)
```bash
peers="6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14156,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
