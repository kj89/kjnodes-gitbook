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

**live-peers** (32)
```
peers="bf16e96a383f317bdc40cdebfdf2a40a7b3d5c9a@142.132.166.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,f851ac3d5d06208bc52cf0ae86b090aa551c5659@80.85.141.82:26656,62c6caafd89eaa885157fc6311b345064f6b1468@185.213.25.129:60956,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,e693197ec64ff270fbee9c5b9d8d055ec6fff1cb@65.21.121.101:46656,45de37d6340caef9bd84111ffb5163d0f3604e84@135.181.153.228:46656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,d0ca7d1e144eee74396b1c7a98737e4ca2ced2bb@137.184.30.252:656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,45cc764ce4547208c21f62340a280cff1f2a4ab5@5.9.147.185:26156,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
