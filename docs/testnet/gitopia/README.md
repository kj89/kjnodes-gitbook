# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```bash
peers="4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,1fee6e7fd077911abab93739f6bf13c62dedbf20@178.62.204.49:26656,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,3727a897b2255c8a2872223af6eb3b9a36d97829@38.242.134.10:10656,d3fe4d63101e72c4cc5fd1114b57d36b759c0402@164.92.72.200:26656,591318ade07c267271bb27790acec9e80dc1ce14@65.21.105.9:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,d238167163e6d34ff8a500afe23386160805d387@193.46.243.144:36656,4432d927cd43ac192701830bed2ba589c6602a7e@165.227.148.44:26656,b5fbf2633a1d00c4e0e62f1e0012f8e72af15aa9@185.218.124.169:26656,a4b24424b94edf6e2b36389b550d5648946535be@178.62.206.89:26656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,2831a266add6225c585d776f2c11bb52cf7d109a@212.90.121.237:26656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,b0eedc8261b3cc7a800cd840bffb9c19b67a05ec@85.190.246.96:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,c865b9d2e12a2388746aa69dda076db984e74c3f@104.248.249.197:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,926b47f8d786e544ec3a9200c61b5b04729a9d57@199.175.98.127:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,bc8a2179df7d5db14504e64cfba8ad4e3d3ce0e4@38.242.156.105:26656,200b0594c8bfd86c1fc2a5b5c72e266139f3b193@62.171.140.239:26656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,d15e22d7be8ba1b97ff429cf87fea2af41450b37@149.102.134.212:41656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,299787b65bc3f176cdfc126af491c282f8e33a85@164.92.107.81:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
