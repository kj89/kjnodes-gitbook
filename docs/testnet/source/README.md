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

**live-peers** (17)
```bash
peers="b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,8574b64414e446621dc9ad09bc25dd328cb6aa2d@184.174.37.152:28656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,f6e7cb4ee4d608822802f58c85e93a7e34ce440d@65.108.237.232:28656,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,4e608992202cfb836a6d69b205bf71cf8c63fd91@75.119.148.0:4003,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
