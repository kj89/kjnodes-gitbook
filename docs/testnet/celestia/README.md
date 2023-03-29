# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.1 | **Wasm**: OFF

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
peers="60e771182358034b4ce475b7a0d8d48734aa9dc8@85.190.134.34:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,23c69377c73644e125d29cb01d1f61e897fc0ae4@65.109.104.70:21066,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,6df4a6d0db5a771b84055646fe3814c655dd3428@95.216.163.64:26656,a1e08e481992149d50cb74144602334e71fa3aa3@62.232.97.106:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,7db3d8fa353b4cf293244f7526cdabfaebef53bf@158.160.24.133:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,3e3d0887865ca6feaf7e99a50dbfb41e591a9781@141.94.138.48:26688,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,63636c9bec15f0039f78bc48736fe8b84e9e8a60@38.242.233.37:26656,5cb79244142c36768571cf1e791578dc45969fd2@195.189.97.33:23656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,43e9da043318a4ea0141259c17fcb06ecff816af@141.94.73.39:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
