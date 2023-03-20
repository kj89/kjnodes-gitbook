# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:20090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (20)
```bash
peers="6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,8ec3dfbfa971264d8cdd86352ffa7bf95d341254@168.119.64.90:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,a1a3fa715c6bc4257613cfbdec06e7d9a0e1edee@65.108.134.175:26656,572cb08735d4572fe62b2fc8b9555c479d8e162f@65.108.137.217:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,6df4a6d0db5a771b84055646fe3814c655dd3428@95.216.163.64:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,e9f81c5428fb9f3645c691dfd3f1038705bbc734@54.160.136.237:26656,02c88d98245ec8b06546f6b19866b758f2df2c6e@95.217.194.249:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,5cb79244142c36768571cf1e791578dc45969fd2@195.189.97.33:23656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
