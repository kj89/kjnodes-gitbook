# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (14)
```bash
peers="1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
