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
peers="f767cc76c0eda6d71b46e02123701364bd3df79c@167.172.39.172:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,a6459b8c3e221e9e0ffd30d8cc883bb2d2d5859f@95.217.16.89:41656,bf16e96a383f317bdc40cdebfdf2a40a7b3d5c9a@142.132.166.131:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,eb5fee5e8d7d5a300db7c89a4a24a205197f85c5@185.237.97.56:656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,8b7f270a398edb7e527eafdbd9781609c79962cf@164.68.106.230:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,45cc764ce4547208c21f62340a280cff1f2a4ab5@5.9.147.185:26156,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,62c6caafd89eaa885157fc6311b345064f6b1468@185.213.25.129:60956,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,f851ac3d5d06208bc52cf0ae86b090aa551c5659@80.85.141.82:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,df5b61e51ab2f6c3bf1f3c387ba1586a84b41b25@141.95.65.26:27956,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,f3289c45d545c589a4114aeeb364fa4c6fde08d9@109.123.254.216:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,965e495f4a69294bd85f3437fccdc9b210fd98b6@1.15.146.92:26656,d491c840bb653847c3ec7b36a3c4493eb8da5be3@167.86.74.218:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
