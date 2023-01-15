# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)


## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: [https://nolus-testnet.grpc.kjnodes.com](https://nolus-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (37)
```bash
peers="7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,9a1d174e1983d56fb40f674fe0e19384ece6320d@194.60.201.171:26656,5c6be03806e01f48b0cd6115f458b9a0d542a3fd@103.166.184.52:26656,58d7fc67e12548f3f1ddda3bbe6000ae3d9d638c@85.10.198.169:13656,ded71439b5a7e377ee272ea7bc3ba132374aa6df@167.86.96.173:27656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,d31acf73c9b1ecf3e7ed78ab2819c3ab40850db0@135.181.116.109:29886,a1e1c8181861c037511186234d459b8de857f25b@103.82.22.221:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,535ca6f6a016261b66ea32c693be35cc3c209414@185.217.125.35:26656,98f1c8de34db535585bfa390151b1d2ab323dc31@167.86.99.207:26656,896c70ce52e6c88313048c9a63fcb9e7f0277144@178.208.86.44:46656,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656,476ec19cf2d9374cdf141a432c7952c57cffadc3@168.119.228.30:26656,19c6579ebb9d869e61c4dd082dc414cac6f799f3@46.4.122.235:26656,18ead126cc62f5aee200a8322b5c97fca6d05880@173.212.194.45:26656,82e7f32dc40a1e7065d11ed3f5d125801baac986@84.46.242.187:26656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,04a0036ff421f2dd8f46cca1fae9a893624bd868@95.216.14.72:29656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,f09a8ba06a00d1edc517995040313732f94c2b56@95.214.55.155:18656,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,2245b73cc59d9d62d00ba17f507675d7e51891ab@185.193.67.93:26656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,ce81aede998514371277a57979712392ffc3d46c@45.142.214.3:37656,a926b4dab08b68abd548b8af00e0582c41ff651b@37.252.80.234:26656,81ff6924175ccca5d1f09cb5d999f0e64852ccea@188.163.121.216:26656,082d7cdc00554199d65f29263663b583f2b8ebc0@209.126.81.240:26656,8af63c83dc832bac3566bd4fca3a197088a7de0f@149.102.146.40:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,d31aa52382bde6978fd1e6dd65496847d0be5a12@147.182.220.109:26656,9fa1e4ded1a41a4498781f93a209053a7c3f36e8@170.187.231.63:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
