# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:28090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (16)
```bash
peers="7a288e8d085b5aad8d43b0c6e6dbb8498588c206@5.182.17.164:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,6e27beffb983b311331f40cf65dfc77afa2fa199@185.250.37.181:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,e2d9b74c65a383a34f9156adb47583e67f996a66@65.109.90.171:28656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
