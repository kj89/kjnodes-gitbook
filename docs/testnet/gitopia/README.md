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

**live-peers** (26)
```
peers="66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,e704537ce1348bfc7b781d6546ae272ff3eea8d5@34.117.96.202:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,54157f773b7135a134b1953d8c8a0ff128cad2f5@194.233.68.165:41656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,e693197ec64ff270fbee9c5b9d8d055ec6fff1cb@65.21.121.101:46656,d2291c87bdef89c31f8e4008ddc0dee2d2a8ef50@143.244.182.43:26656,fbd3b296871ae841b638158e29d48e09180b7c4e@194.233.77.238:41656,e87b6771feff9f3c41e23a7c1e42b507345505fb@194.34.232.99:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,a6459b8c3e221e9e0ffd30d8cc883bb2d2d5859f@95.217.16.89:41656,8a86d39f08c47ed0ef2bd21606f16817744a3742@38.242.203.117:26656,89cb3e8c242246903f4b57c472d5866f8d29b4b6@109.123.242.208:27656,a4eefa82608b31b55b70307f3db0d88261d8ed9b@154.53.57.72:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
