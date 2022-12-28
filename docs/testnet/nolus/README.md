# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)


## Public endpoints

* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (37)
```
peers="3cadae7324e9bf129b76bc489cd080535d03f3d2@176.9.22.117:55656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d53006a0db9a2eac79f853526719716cece550ad@144.76.92.112:26656,8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,89aaf76a23b16bd57a1982e7b304fd998a49942a@65.109.85.226:9000,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,c8c6249b27b4a34aac554d12b0107cc6421098ef@65.108.126.35:24656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,476ec19cf2d9374cdf141a432c7952c57cffadc3@168.119.228.30:26656,8ca0bffdf45aa4aaa4624c6d4c3e258a8c595591@65.108.43.58:27659,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656,301dcb25951a0ebd6a36e09e612c85dc3aea3767@95.70.160.37:26656,d788696b4ea9ddd295f86f0cb10a6be86a94764c@161.97.136.72:26656,d694df8e90ddf6102be5c825e57fc58d55217629@143.198.205.193:26656,d0d604e5c22d5be38adaea41fc9694a26dc143ac@217.79.255.69:26656,e17967a4b9a8183d12659fab318a4f81673f6a51@185.245.183.172:37656,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,2c5145c500078fae0e6c013ef75afad62c3c0ea2@95.128.140.24:26656,ef404b6e855c70ee51532ca83407350d2379bdec@5.161.101.185:26656,e0ea5572b54c2bb5860304c5f0163becd78fee7c@178.20.44.3:43656,2e3df91be55a88d53a26161e1e3314aff8889593@108.175.1.130:29656,ac38d6ef4cc254c689bcd6bcaf2a359672e4405b@77.238.148.219:26656,b5a5b708db94c3d73a05a0fc1eb5509073f5920c@185.209.31.23:43656,c4a974e2a4d548163e6506f2d2f2d4aeb1c89f18@194.163.190.167:36656,1e679cdba975c9cdd60b764d498b70518b8f6678@89.252.21.37:26656,ea777d59ec44f1739c6a4908942db43966a1f475@45.55.59.70:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:15256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
