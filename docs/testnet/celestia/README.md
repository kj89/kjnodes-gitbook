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
peers="da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,3e3d0887865ca6feaf7e99a50dbfb41e591a9781@141.94.138.48:26688,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,384266dddab82417fb12ac44a9bdd36578a9cf0c@185.255.131.173:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,02c88d98245ec8b06546f6b19866b758f2df2c6e@95.217.194.249:26656,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,1f05828ec9264cfa83454b0176414006bd40dce3@162.19.171.122:26656,a1a3fa715c6bc4257613cfbdec06e7d9a0e1edee@65.108.134.175:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,9fd9275b49d478bf8352dc160dc0e9a184011098@217.182.194.152:26656,68a87c501de64b9259a0023d20fb805dff89082e@13.58.18.103:31380,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,dee24c88c902ae0b117141f3b1e696b5c92d8e51@57.128.74.73:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
