# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)




## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: [https://celestia-testnet.grpc.kjnodes.com](https://celestia-testnet.grpc.kjnodes.com)

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
peers="5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,cc167c48a977160de9f9bbb5c3b80ddb7d585a67@176.9.156.135:26656,d78275c79f81efc0eb357cec3ec35877efec4974@57.128.74.131:26656,3e3d0887865ca6feaf7e99a50dbfb41e591a9781@141.94.138.48:26688,1f05828ec9264cfa83454b0176414006bd40dce3@162.19.171.122:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30590,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,2b749c2f0dd5953eeb5379c7ae7a15ed1020f7e5@135.181.136.124:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,6f3b4a8311463a03805fc6dcf48ea00b3f84357e@65.108.234.207:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,a1e08e481992149d50cb74144602334e71fa3aa3@62.232.97.106:26656,dee24c88c902ae0b117141f3b1e696b5c92d8e51@57.128.74.73:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
