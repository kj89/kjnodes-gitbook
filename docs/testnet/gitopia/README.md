# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,c0e48b5f3ab79c24f1594f5a0d67a7a3f717882a@91.223.3.144:26456,980e2ec8f4ddba44e4a928452e49f3cae722fce3@65.21.182.244:27656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,afbed8b52881b2f783df0cb07865a4da2fbbdf5e@167.235.243.27:26656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,e1a8a4cdb6281c434d86b85f3e66c5f7b899abf6@95.217.183.63:27656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,848d1905d86a576f26371c0d3c5e07502f2c5887@65.21.104.54:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,0f64a56a1d4a4fa1407f2ac4533f2de67a0959d1@95.217.144.25:15609,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,b19cf9ffb92876b32e18a97d092e08565e40899b@185.216.203.66:41656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,42ba206efd9dd10847fa20f09a74fde6706442aa@194.146.13.128:60956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
